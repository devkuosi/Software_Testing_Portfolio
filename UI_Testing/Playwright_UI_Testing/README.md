# 🎯 TaskForge E2E Testing Suite with Playwright

This repository demonstrates a **production-level End-to-End (E2E) test suite** using [Playwright](https://playwright.dev/) for a simulated SaaS productivity platform called **TaskForge**.

The goal is to showcase advanced QA and automation practices, with a focus on realistic user flows, role-based testing, external API mocking, file operations, real-time WebSocket validation, and responsive layout testing.

---

## 🧪 About the Project

**System Under Test (SUT): TaskForge**

A fictional SaaS task management platform similar to Trello/Asana, featuring:
- Multi-role access (Admin, Manager, Contributor)
- Real-time task boards (WebSocket-powered)
- File collaboration (upload/download)
- External integrations (Google Calendar, Slack)
- PWA + offline mode
- Responsive UI (Mobile/Tablet/Desktop)

---

## 🔍 What This Test Suite Covers

| Area                 | Features Tested |
|----------------------|------------------|
| 🔐 Authentication     | Role-based login for Admin, Manager, and User |
| 📋 Task Boards        | Create, assign, filter, drag-and-drop, real-time sync |
| 📁 File Handling      | Upload (PDFs), Download, Audit trails |
| 📤 Notifications      | Mocked email + in-app notifications |
| 🌐 API Integrations   | Google Calendar (mocked), SendGrid |
| 📱 Responsive Layout  | Viewport switching for mobile/tablet/desktop |
| 📴 Offline Mode       | PWA testing with no network connection |
| ⚡ Performance        | Parallel test execution with isolated sessions |

---

## 📁 Folder Structure


```bash
tests/
├── auth/
│   └── rbac-login.spec.ts
├── boards/
│   ├── create-board.spec.ts
│   ├── drag-drop-columns.spec.ts
│   └── real-time-updates.spec.ts
├── files/
│   ├── upload-verify.spec.ts
│   └── download-audit.spec.ts
├── notifications/
│   └── email-inapp-mocking.spec.ts
├── integration/
│   └── calendar-sync.spec.ts
├── offline/
│   └── pwa-mode.spec.ts
├── responsive/
│   └── mobile-tablet-layout.spec.ts
├── utils/
│   ├── fixtures.ts
│   └── roles.ts
└── assets/
    └── test-doc.pdf
```