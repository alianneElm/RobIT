# 🔐 Security Policy

## Supported Versions

RobIT is a demo project maintained as part of a technical showcase. While not intended for production use, we still take security and responsible disclosure seriously.

| Version        | Supported | Notes                          |
| -------------- | --------- | ------------------------------ |
| `main`         | ✅         | Actively developed and patched |
| `v1.3.0`       | ✅         | Latest stable release          |
| Prior versions | ❌         | Deprecated / development-only  |

⚠️ Security updates will only be applied to the main branch and the latest stable release (v1.3.0).
Please update to the latest version to receive fixes and improvements.

---

## Reporting a Vulnerability

If you discover a security vulnerability or any behavior that might pose a risk, please follow these steps:

1. **Do not open a public issue.**
2. Instead, contact us **privately** via email: `alianneelm@yahoo.se`
3. Include as many details as possible:
   - Steps to reproduce
   - Affected component (if known)
   - Severity assessment
   - Screenshots or logs if applicable

---

## Security Best Practices

Although RobIT is a CLI-only educational tool, it follows these practices:

- No network access or external inputs
- No file I/O or persistence by default
- Code is fully test-covered and linted
- All logic runs within sandboxed input prompts

---

## Disclosure Timeline

We will publicly disclose and patch critical issues in the next tagged release once verified and resolved.

Thank you for helping make open-source software better and safer!  
— Alianne Elm

