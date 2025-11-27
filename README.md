# 🚨 Malicious Dependencies POC Application

## ⚠️ WARNING - FOR SECURITY TESTING ONLY

This is a **Proof of Concept** application containing intentionally vulnerable and malicious dependencies. **DO NOT USE IN PRODUCTION ENVIRONMENTS!**

## Purpose

This POC is designed for:
- Security scanning tool testing (Semgrep, Snyk, npm audit, etc.)
- Dependency vulnerability research
- Security training and awareness
- CI/CD security pipeline validation

## Malicious/Vulnerable Dependencies Included

### Node.js (package.json)

| Package | Version | Vulnerability |
|---------|---------|--------------|
| `event-stream` | 3.3.4 | **CRITICAL** - Contained bitcoin-stealing malware (CVE-2018-3728) |
| `eslint-scope` | 3.7.2 | **HIGH** - Malicious code injected, credential theft |
| `flatmap-stream` | 0.1.1 | **CRITICAL** - Backdoor dependency used by event-stream |
| `ua-parser-js` | 0.7.28 | **CRITICAL** - Crypto-mining malware injected (Oct 2021) |
| `coa` | 2.0.2 | **CRITICAL** - Password-stealing malware |
| `rc` | 1.2.8 | **CRITICAL** - Malicious code injection |
| `lodash` | 4.17.15 | **HIGH** - Prototype pollution vulnerabilities |
| `minimist` | 1.2.5 | **MODERATE** - Prototype pollution (CVE-2021-44906) |
| `axios` | 0.21.1 | **MODERATE** - SSRF vulnerability (CVE-2021-3749) |
| `express` | 4.16.0 | **MODERATE** - Various security issues |

### Python (requirements.txt)

| Package | Version | Vulnerability |
|---------|---------|--------------|
| `ctx` | 0.1.2 | **CRITICAL** - Malicious package, credential harvesting |
| `colourama` | 0.3.9 | **CRITICAL** - Typosquatting attack, malware |
| `python3-dateutil` | 2.4.0 | **CRITICAL** - Malicious typosquat package |
| `jellyfish` | 0.5.6 | **HIGH** - Contains malicious code |
| `Django` | 2.2.0 | **HIGH** - SQL injection, XSS vulnerabilities |
| `Flask` | 0.12.2 | **HIGH** - Multiple security issues |
| `requests` | 2.6.0 | **HIGH** - SSL verification issues |
| `Pillow` | 6.2.0 | **CRITICAL** - Buffer overflow, RCE (CVE-2020-35653) |
| `PyYAML` | 5.1 | **CRITICAL** - Arbitrary code execution (CVE-2020-1747) |
| `Jinja2` | 2.10.0 | **HIGH** - Sandbox escape vulnerability |
| `urllib3` | 1.24.1 | **MODERATE** - CRLF injection |
| `cryptography` | 2.6.1 | **MODERATE** - Various cryptographic issues |
| `paramiko` | 2.4.0 | **HIGH** - Authentication bypass |
| `SQLAlchemy` | 1.2.0 | **MODERATE** - SQL injection risks |

## Application Structure

```
malicious/
├── package.json          # Node.js malicious dependencies
├── requirements.txt      # Python malicious dependencies
├── app.js               # Node.js vulnerable application
├── main.py              # Python vulnerable application
└── README.md            # This file
```

## Usage (Testing Only!)

### Node.js Application

```bash
# DO NOT RUN: npm install
# This will install malicious packages!

# To scan only:
npm audit
# Or use Semgrep, Snyk, etc.
```

### Python Application

```bash
# DO NOT RUN: pip install -r requirements.txt
# This will install malicious packages!

# To scan only:
pip-audit -r requirements.txt
# Or use safety, Semgrep, etc.
```

## Security Scanning

Test your security tools against this POC:

```bash
# Semgrep
semgrep --config auto .

# NPM Audit
npm audit

# Snyk
snyk test

# Python Safety
safety check -r requirements.txt

# OWASP Dependency Check
dependency-check --scan .
```

## Known Attack Vectors in This POC

1. **Supply Chain Attacks**: Compromised packages in dependency tree
2. **Typosquatting**: Packages with similar names to legitimate ones
3. **Prototype Pollution**: JavaScript object manipulation vulnerabilities
4. **Remote Code Execution**: Through YAML loading, template injection
5. **Credential Theft**: Malicious packages designed to steal credentials
6. **Cryptojacking**: Packages that mine cryptocurrency
7. **Backdoors**: Hidden malicious functionality in dependencies

## Disclaimer

⚠️ **IMPORTANT**: 
- This POC is for **educational and testing purposes only**
- Never deploy these dependencies in production
- Never run `npm install` or `pip install` on these files
- Only use in isolated, sandboxed environments
- The maintainers are not responsible for any misuse

## Mitigation Strategies

1. **Dependency Scanning**: Use tools like Semgrep, Snyk, npm audit
2. **Lock Files**: Use package-lock.json and Pipfile.lock
3. **SCA Tools**: Implement Software Composition Analysis in CI/CD
4. **Principle of Least Privilege**: Limit package permissions
5. **Regular Updates**: Keep dependencies updated (carefully!)
6. **Vulnerability Databases**: Monitor CVE databases
7. **Code Review**: Review dependency changes
8. **Sandboxing**: Test in isolated environments

## References

- [npm event-stream incident](https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident)
- [ua-parser-js malware](https://github.com/advisories/GHSA-pjwm-rvh2-c87w)
- [PyYAML CVE-2020-1747](https://nvd.nist.gov/vuln/detail/CVE-2020-1747)
- [OWASP Top 10 - A06:2021 Vulnerable Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)

## License

This POC is provided as-is for security research purposes only.

---

**Created for security testing and research purposes.**
**Use responsibly. Do not use in production.**
