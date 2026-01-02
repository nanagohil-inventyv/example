Modules for the project you are assigned are as follows (Please take a note, this is just high-level and basic descriptions, it is subjected to change depending on the requirements change):
 
## Module 1: Unified Chat System
 
- Team Size: 5
 
- Definition
  - A real-time messaging system supporting 1:1 chats, group chats, channels, and customer support chats.
 
- Abstract
  - This module replaces fragmented chat tools by offering a single chat backbone for employees, cross-country teams, and customers - without leaking data to third-party platforms.
 
- Scope
  - WebSocket-based real-time messaging (Rust)
  - Channel-based access control
  - Country-aware presence
  - Customer <-> Support agent chat isolation
  - Angular chat UI with threads, mentions, reactions
  - Message retention policies
 
## Module 2: Video Conferencing
 
- Team Size: 5
 
- Definition
  - Browser-based video conferencing for internal meetings, tax consultations, and customer support calls.
 
- Abstract
  - A secure, lightweight video system that avoids vendor lock-in while supporting multi-region participation, session recording, and role-based access.
 
- Scope
  - WebRTC signaling server (Rust)
  - Room creation & joining
  - Role-based permissions (host, participant, guest)
  - Recording hooks (store metadata, not raw video initially)
  - Angular meeting UI
  - Country latency awareness (basic routing logic)
 
## Module 3: Secure File Sharing
 
- Team Size: 4
 
- Definition
  - A controlled file-sharing system for documents, media, and reports, usable internally and with customers.
 
- Abstract
  - Files are where companies accidentally destroy themselves. This module ensures auditability, access control, and traceability.
 
- Scope
  - File upload/download service (Rust)
  - Object storage integration
  - File permissions per user / group / customer
  - Versioning metadata
  - Angular file manager UI
  - Activity logs (who touched what, when, (optional))
 
## Module 4: AI Integration Module & Internal Alerting with Notification System
 
- Team Size: 4
 
- Definition (AI Integration Module)
  - AI-powered assistance embedded across chat, meetings, and files.
 
- Abstract (AI Integration Module)
  - AI here is not a toy chatbot - it's a copilot that reduces human misunderstanding and repetitive work.
 
- Scope (AI Integration Module)
  - AI service abstraction layer (Rust)
  - Chat summarization
  - Meeting notes generation
  - File content Q&A
  - Angular AI assistant panel
  - Plug-in ready (OpenAI for starters then local LLM later)
 
- Definition (Internal Alerting with Notification System)
  - A centralized alerting system for system alerts, internal announcements, compliance warnings, and emergencies.
 
- Abstract (Internal Alerting with Notification System)
  - Pings are noises not alerts, where as this module creates signals which are actionable.
 
- Scope (Internal Alerting with Notification System)
  - Priority-based alerts (info / warning / critical)
  - Targeted alerts (team, country, role)
  - Read receipts & acknowledgment tracking
  - Angular notification center
  - Rust scheduler + event triggers
 
## Module 5: Remote Support & Screen Assistance
 
- Team Size: 5
 
- Definition
  - Secure remote access for IT support and customer assistance without external tools.
 
- Abstract
  - This module enables on-demand support sessions while maintaining strict consent and auditing, crucial for enterprise and tax-related environments.
 
- Scope
  - Session initiation & approval flow
  - Temporary access tokens
  - Screen-sharing signaling (no raw OS hooks yet)
  - Session logging
  - Angular support dashboard
  - Customer-side lightweight web access
 
## Module 6: Cross-Country Collaboration Layer
 
- Team Size: Shared responsibility (Architectural)
 
- Definition
  - A system layer ensuring smooth collaboration across time zones, regions, and compliance boundaries.
 
- Abstract
  - Global teams fail not because of distance, but because systems pretend distance doesn't exist.
 
- Scope
  - Time-zone aware scheduling
  - Region tagging on users & data
  - GDPR-friendly data flags
  - Country-based feature toggles
  - Visible overlap hours in UI