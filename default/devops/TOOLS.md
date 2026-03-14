---
updated: 2026-03-12 | 14:30
created: 2026-03-12 | 13:14
---
# Tools

(Your tools will go here. Add notes about them as you acquire and use them.)

## Infrastructure & Provisioning

- **Infrastructure as Code**: Terraform, AWS CloudFormation, Pulumi for infrastructure automation.
- **Configuration Management**: Ansible, Chef, Puppet, SaltStack for system configuration.
- **Cloud Platforms**: AWS, Google Cloud Platform, Azure, DigitalOcean for hosting.
- **Serverless**: AWS Lambda, Google Cloud Functions, Vercel, Netlify.
- **Container Orchestration**: Kubernetes, Docker Swarm, ECS, Nomad.
- **Service Mesh**: Istio, Linkerd, Consul Connect.
- **Edge CDN**: Cloudflare, Fastly, AWS CloudFront for content delivery.
- **DNS Management**: Cloudflare DNS, Route 53, Google Cloud DNS.

## Monitoring & Observability

- **Metrics Collection**: Prometheus, StatsD, Telegraf, OpenTelemetry.
- **Visualization**: Grafana, Datadog, CloudWatch Dashboards.
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana), Loki, Splunk, Papertrail.
- **Tracing**: Jaeger, Zipkin, OpenTelemetry tracing, Honeycomb.
- **Alerting**: Alertmanager, PagerDuty, Opsgenie, VictorOps.
- **Synthetic Monitoring**: Checkly, UptimeRobot, Pingdom, New Relic Synthetics.
- **Real User Monitoring**: Google Analytics, Mixpanel, PostHog, FullStory.
- **Error Tracking**: Sentry, Bugsnag, Rollbar, Raygun.

## Automation & Orchestration

- **CI/CD Platforms**: GitHub Actions, GitLab CI, Jenkins, CircleCI, Buildkite.
- **Workflow Automation**: n8n, Zapier, Make (Integromat), Huginn.
- **GitOps**: ArgoCD, FluxCD for Kubernetes deployments.
- **Scheduled Jobs**: Cron, systemd timers, AWS EventBridge.
- **Infrastructure Testing**: Terratest, Kitchen-Terraform, ServerSpec.
- **ChatOps**: Slack bots, Discord bots for operational commands.

## Content Delivery & Distribution

- **File Sync**: rsync, lsyncd, Syncthing for file synchronization.
- **Object Storage**: AWS S3, Google Cloud Storage, Backblaze B2.
- **Static Site Hosting**: Hugo, Jekyll, Next.js static exports to Netlify/Vercel.
- **Content Publishing**: Hugo server, Jekyll build, WordPress REST API.
- **RSS Generation**: Feed generators for content distribution.
- **Email Delivery**: SendGrid, Postmark, Amazon SES, Mailgun.
- **Webhook Management**: webhook.site, ngrok for testing webhooks.

## Backup & Recovery

- **Backup Tools**: restic, duplicity, BorgBackup, Rclone.
- **Database Backups**: pg_dump, mysqldump, mongodump with automation.
- **Snapshot Management**: Cloud provider snapshots, Velero for Kubernetes.
- **Backup Verification**: Automated restore testing procedures.
- **Offsite Storage**: S3, Google Cloud Storage, Backblaze B2 for backup storage.
- **Backup Monitoring**: Custom scripts, backup status dashboards.

## Cost Management & Optimization

- **Cloud Cost Tools**: CloudHealth, CloudCheckr, Cloudability, native cloud cost explorers.
- **Resource Monitoring**: AWS Cost Explorer, Google Cloud Billing reports.
- **Spend Alerts**: Budget alerts, anomaly detection for spending.
- **Right-sizing**: Tools to optimize resource allocation.
- **Reserved Instances**: RI/Savings Plans management.
- **Cost Allocation**: Tagging strategies and cost center reporting.

## Security & Compliance

- **Secrets Management**: HashiCorp Vault, AWS Secrets Manager, Doppler.
- **Container Security**: Trivy, Clair, Anchore, Snyk container.
- **Vulnerability Scanning**: Snyk, Dependabot, OWASP Dependency-Check.
- **Security Hardening**: CIS Benchmarks, OpenSCAP, security baselines.
- **Access Management**: IAM, LDAP, Active Directory integration.
- **SSO**: Auth0, Okta, Keycloak for single sign-on.
- **Audit Logging**: Cloud audit logs, SIEM integration.
- **Compliance**: Chef InSpec, Open Policy Agent for compliance as code.

## Database Operations

- **Database Management**: pgAdmin, MongoDB Compass, MySQL Workbench.
- **Database Migration**: Flyway, Liquibase, Alembic, Django migrations.
- **Replication Management**: Monitor and manage database replication.
- **Connection Pooling**: PgBouncer, ProxySQL for connection management.
- **Backup Automation**: Automated database backup scripts and schedules.
- **Performance Monitoring**: pg_stat_statements, slow query logs.

## Network & Connectivity

- **Network Monitoring**: nmap, ping, MTR for connectivity testing.
- **Firewall Management**: iptables, ufw, cloud security groups.
- **Load Balancing**: HAProxy, Nginx, AWS ALB, Google Cloud Load Balancer.
- **VPN & Tunneling**: OpenVPN, WireGuard, Tailscale for secure connections.
- **DNS Tools**: dig, nslookup, nsupdate for DNS management.
- **Certificate Management**: certbot, acme.sh for SSL/TLS certificates.

## Documentation & Runbooks

- **Documentation Sites**: Docusaurus, MkDocs, Hugo for operational docs.
- **Internal Wiki**: Confluence, Notion, Obsidian for operational knowledge.
- **Runbook Templates**: Standardized templates for incident response.
- **Procedure Documentation**: Step-by-step guides for common operations.
- **Architecture Diagrams**: Mermaid, PlantUML, diagrams.net for system diagrams.
- **API Documentation**: Swagger UI, Redoc for internal APIs.

## Team Collaboration

- **Communication**: Slack, Microsoft Teams, Discord for team chat.
- **Meeting Tools**: Zoom, Google Meet for video conferencing.
- **Screen Sharing**: Screen sharing tools for incident collaboration.
- **Pair Programming**: CodeWith, Tuple for remote pairing.
- **Miro/Mural**: Virtual whiteboards for system design sessions.
- **On-call Rotations**: Schedule management for operations coverage.

## Performance & Reliability

- **Load Testing**: k6, Locust, JMeter for performance testing.
- **Chaos Engineering**: Chaos Mesh, Gremlin, Pumba for resilience testing.
- **Capacity Planning**: Forecasting tools and load analysis.
- **Performance Profiling**: APM tools like New Relic, Datadog APM.
- **Database Tuning**: Query optimization and index management.

## Vendor & Service Management

- **Service Catalog**: Track all third-party services and subscriptions.
- **Vendor Management**: Contract tracking and renewal management.
- **API Management**: API gateways and integration management.
- **SLA Monitoring**: Track vendor performance against SLAs.

## Quality Assurance

- **Test Environments**: Staging and pre-production environments.
- **Change Management**: Change request processes and approvals.
- **Deployment Gates**: Quality gates before production deployment.
- **Post-Deployment Verification**: Smoke tests and health checks.
- **Rollback Procedures**: Automated rollback scripts and procedures.

## Emergency Response

- **Incident Management**: Incident.io, Jira Service Management for tracking.
- **On-call Management**: PagerDuty, Opsgenie for alert routing.
- **War Rooms**: Dedicated channels for major incident response.
- **Communication Templates**: Pre-written templates for status updates.
- **Post-Mortem Templates**: Structured post-incident review process.
- **Disaster Recovery**: DR runbooks and failover procedures.

## Compliance & Auditing

- **Audit Trails**: Centralized logging for compliance requirements.
- **Policy Enforcement**: Open Policy Agent, Sentinel for policy as code.
- **Compliance Scans**: automated compliance checking tools.
- **Evidence Collection**: Tools for collecting compliance evidence.
- **Access Reviews**: Regular access review processes and tools.

## Cost Optimization Practices

- **Resource Tagging**: Consistent tagging for cost allocation.
- **Auto-scaling**: Configure auto-scaling for variable workloads.
- **Spot Instances**: Use spot/preemptible instances for non-critical workloads.
- **Reserved Capacity**: Purchase reserved instances for baseline capacity.
- **Storage Tiering**: Move old data to cheaper storage tiers.
- **Idle Resource Detection**: Identify and clean up unused resources.

## Skills to Develop

- **Scripting**: Bash, Python for automation tasks.
- **Infrastructure as Code**: Terraform or alternative.
- **Container Orchestration**: Kubernetes fundamentals.
- **Cloud Services**: Deep knowledge of chosen cloud provider.
- **Monitoring**: Prometheus + Grafana stack.
- **Incident Response**: calm under pressure, clear communication.
- **Documentation**: Clear, actionable runbooks.
- **Cost Management**: Cloud cost optimization techniques.
- **Security**: Security best practices and tools.
- **Networking**: Understanding of networks, firewalls, load balancers.

## Operational Principles

- Automate everything repeatable
- Monitor everything that matters
- Document everything critical
- Test everything that could break
- Plan for failure before designing for success
- Keep it simple; complexity is the enemy of reliability
- Assume nothing; verify everything
- Treat infrastructure as product
- Continuous improvement through blameless post-mortems
- Share knowledge; avoid single points of failure
- Cost awareness in all decisions
- Security is not optional

This list will evolve as you acquire and use new tools. As Ops, you should be evaluating tools that improve reliability, reduce toil, and optimize costs. Keep your toolkit current and document tool usage clearly for team knowledge sharing.
