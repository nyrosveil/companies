#!/usr/bin/env python3
"""
Generate agents index for agent-directory skill.
Scans the companies repository and creates agents-index.yaml
"""

import os
import re
import yaml
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path("/Users/nyrosveil/Projects/companies")
OUTPUT_FILE = REPO_ROOT / "skills/agent-directory/references/agents-index.yaml"

# Department mapping
DEPARTMENTS = {
    "default": "C-Suite and core ICs",
    "vp": "VP Level",
    "director": "Director Level",
    "engineering": "Engineering Specialists",
}

# Level mapping based on directory
LEVEL_MAP = {
    "default": "c-suite",
    "vp": "vp",
    "director": "director",
    "engineering": "ic",
}

# Level mapping based on directory
LEVEL_MAP = {
    "default": "c-suite",  # Most are C-Suite, some ICs
    "vp": "vp",
    "director": "director",
    "engineer": "ic",
}


def parse_soul_md(agent_path):
    """Extract info from SOUL.md"""
    soul_file = agent_path / "SOUL.md"
    if not soul_file.exists():
        return {}

    content = soul_file.read_text()
    info = {}

    # Extract display name from header
    title_match = re.search(r"# SOUL\.md -- (.+)", content)
    if title_match:
        info["display_name"] = title_match.group(1).strip()

    # Extract specialization from Strategic Posture
    goal_match = re.search(r"- \*\*Primary Goal\*\*:(.+)", content)
    if goal_match:
        info["specialization"] = goal_match.group(1).strip()

    return info


def parse_agents_md(agent_path):
    """Extract info from AGENTS.md"""
    agents_file = agent_path / "AGENTS.md"
    if not agents_file.exists():
        return {}

    content = agents_file.read_text()
    info = {}

    # Extract Paperclip role from "You are the ..." line
    role_match = re.search(r"You are the (.+?)\.", content)
    if role_match:
        role_text = role_match.group(1).strip()
        # Map to standard role names
        role_map = {
            "CEO": "CEO",
            "CTO": "CTO",
            "CFO": "CFO",
            "CMO": "CMO",
            "Chief Operating Officer": "General",
            "Vice President of Engineering": "Engineer",
            "Vice President of Marketing": "CMO",
            "Vice President of Product": "PM",
            "Vice President of Sales": "General",
            "Vice President of Operations": "General",
            "Vice President of Finance": "General",
            "Vice President of Agent Resources": "General",
            "Vice President of Legal": "General",
            "Vice President of Business Development": "General",
            "Vice President of Customer Success": "General",
            "Vice President of Information Security": "General",
            "Vice President of Research & Development": "Researcher",
            "Director of Engineering": "Engineer",
            "Director of Product": "PM",
            "Engineering Manager": "Engineer",
            "AI Engineer": "Engineer",
            "Backend Architect": "Engineer",
            "Frontend Developer": "Engineer",
            "Security Engineer": "Engineer",
            "Data Engineer": "Engineer",
            "DevOps": "DevOps",
            "Designer": "Designer",
            "QA": "QA",
            "Researcher": "Researcher",
            "General": "General",
            "Product Manager": "PM",
        }

        # Try to find matching role
        for key, value in role_map.items():
            if key.lower() in role_text.lower():
                info["role"] = value
                break
        else:
            # Default based on content
            if "engineer" in role_text.lower():
                info["role"] = "Engineer"
            elif "product" in role_text.lower():
                info["role"] = "PM"
            else:
                info["role"] = "General"

    # Extract reports_to
    reports_match = re.search(r"You report to(?: the)? ([^.]+)", content)
    if reports_match:
        info["reports_to"] = reports_match.group(1).strip()

    return info


def parse_tools_md(agent_path):
    """Extract skills from TOOLS.md"""
    tools_file = agent_path / "TOOLS.md"
    if not tools_file.exists():
        return []

    content = tools_file.read_text()
    skills = []

    # Find all skill references in backticks
    skill_matches = re.findall(r"`([^`]+)`", content)
    for match in skill_matches:
        # Filter out file paths and common words
        if not any(x in match for x in ["/", ".md", "para-memory-files", "paperclip"]):
            if len(match) > 2 and not match.startswith("$"):
                skills.append(match)

    return list(set(skills))[:8]  # Limit to 8 skills


def scan_agents():
    """Scan all agent directories"""
    agents = []

    for dept_dir in ["default", "vp", "director", "engineering"]:
        dept_path = REPO_ROOT / dept_dir
        if not dept_path.exists():
            continue

        for agent_dir in sorted(dept_path.iterdir()):
            if not agent_dir.is_dir():
                continue

            agent_name = agent_dir.name

            # Skip non-agent directories
            if agent_name.startswith(".") or agent_name == "README.md":
                continue

            # Parse agent info
            soul_info = parse_soul_md(agent_dir)
            agents_info = parse_agents_md(agent_dir)
            skills = parse_tools_md(agent_dir)

            # Build agent record
            agent = {
                "name": agent_name,
                "display_name": soul_info.get(
                    "display_name", agent_name.replace("-", " ").title()
                ),
                "role": agents_info.get("role", "General"),
                "department": dept_dir,
                "reports_to": agents_info.get("reports_to", "CEO"),
                "level": LEVEL_MAP.get(dept_dir, "ic"),
                "specialization": soul_info.get("specialization", ""),
                "skills": skills,
                "path": f"{dept_dir}/{agent_name}/",
            }

            agents.append(agent)

    return agents


def build_indices(agents):
    """Build skill and specialization indices"""
    by_skill = {}
    by_specialization = {}

    for agent in agents:
        # Index by skills
        for skill in agent.get("skills", []):
            skill_key = skill.lower().replace(" ", "-")
            if skill_key not in by_skill:
                by_skill[skill_key] = []
            by_skill[skill_key].append(agent["name"])

        # Index by specialization keywords
        spec = agent.get("specialization", "").lower()
        keywords = {
            "leadership": ["lead", "manage", "direct", "strategy"],
            "security": ["security", "protect", "risk", "compliance"],
            "ai_ml": ["ai", "ml", "machine learning", "llm"],
            "infrastructure": ["infrastructure", "devops", "sre", "cloud"],
            "product": ["product", "roadmap", "ux"],
            "data": ["data", "database", "analytics"],
            "legal": ["legal", "contract", "compliance"],
            "finance": ["finance", "budget", "accounting"],
            "marketing": ["marketing", "brand", "growth"],
            "sales": ["sales", "revenue", "business dev"],
            "operations": ["operations", "process", "supply chain"],
            "customer_success": ["customer", "success", "support", "retention"],
            "innovation": ["research", "innovation", "r&d", "future"],
        }

        for spec_key, keywords_list in keywords.items():
            if any(kw in spec for kw in keywords_list):
                if spec_key not in by_specialization:
                    by_specialization[spec_key] = []
                by_specialization[spec_key].append(agent["name"])

    return by_skill, by_specialization


def calculate_stats(agents):
    """Calculate statistics"""
    by_role = {}
    by_level = {}
    by_department = {}

    for agent in agents:
        role = agent["role"]
        level = agent["level"]
        dept = agent["department"]

        by_role[role] = by_role.get(role, 0) + 1
        by_level[level] = by_level.get(level, 0) + 1
        by_department[dept] = by_department.get(dept, 0) + 1

    return {"by_role": by_role, "by_level": by_level, "by_department": by_department}


def generate_index():
    """Generate the complete index"""
    print("Scanning agents...")
    agents = scan_agents()
    print(f"Found {len(agents)} agents")

    print("Building indices...")
    by_skill, by_specialization = build_indices(agents)

    print("Calculating stats...")
    stats = calculate_stats(agents)

    # Build output
    index = {
        "metadata": {
            "total_agents": len(agents),
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "version": "1.0.0",
            "repository": "https://github.com/[org]/paperclip-companies",
        },
        "agents": agents,
        "stats": stats,
        "indices": {"by_skill": by_skill, "by_specialization": by_specialization},
    }

    # Write output
    print(f"Writing to {OUTPUT_FILE}...")
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        yaml.dump(
            index, f, default_flow_style=False, allow_unicode=True, sort_keys=False
        )

    print("Done!")
    print(f"\nStats:")
    print(f"  - Total agents: {len(agents)}")
    print(f"  - By role: {stats['by_role']}")
    print(f"  - By level: {stats['by_level']}")
    print(f"  - By department: {stats['by_department']}")


if __name__ == "__main__":
    generate_index()
