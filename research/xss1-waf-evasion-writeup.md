# Writeup1: Bypassing Hardened Server-Side WAF to Achieve Reflected XSS

## 1. Executive Summary
This research documents the discovery and successful exploitation of a **Reflected Cross-Site Scripting (XSS)** vulnerability on a simulated government portal for the fabled United Republic of Neo-Valkyria. Although the developer implemented an aggressive, blacklist-based Web Application Firewall (WAF) regex mechanism on the backend, the protective layers were logically bypassed. This was achieved by exploiting client-side browser internals and behavior patterns found in modern JavaScript syntax.

## 2. Attack Vector Analysis (The Constraints)
During initial reconnaissance and active fuzzing of the HTTP GET parameter `?path=`, the backend infrastructure immediately drops the session (returning an HTTP 403 Forbidden status) if it intercepts any of the following malicious payload signatures:

| Security Control | Targeted WAF Mechanism | Impact on Standard Payloads |
| :--- | :--- | :--- |
| **Signature Blocking** | Detects sensitive keywords such as `alert`, `prompt`, and `confirm`. | Blocks native JavaScript pop-up handlers traditionally used for Proof-of-Concepts. |
| **Token Restriction** | Strictly prohibits the use of parentheses `()` characters. | Halts operational functional execution flows entirely. |
| **Sanitization Filter** | Automatically strips the `<script>` tag (case-insensitive). | Destroys traditional script tag injection vectors. |
| **Whitespace Constraint** | Rejects requests containing literal space characters (` `). | Defeats the insertion of space-separated HTML attributes. |

---

## 3. Evasion Methodology (How the Bypass Works)
To circumvent the defensive architecture outlined above, a multi-stage evasion strategy was engineered by leveraging specific parsing behaviors within the browser engine:

### 💡 Whitespace Elimination
Instead of utilizing a traditional space character to separate the HTML tag name from the event handler, the payload utilizes a forward slash (`/`). The browser parser natively treats the slash as a valid attribute boundary, rendering the tag properly.
* *Vector:* `<svg/onload=...>`

### 💡 Regex Signature Deflection (Dynamic String Construction)
Because the WAF actively blacklists the raw string `alert`, the payload manipulates the global window scope object via JavaScript's `top` reference. In JavaScript, functions can be accessed as array properties using **Bracket Notation** combined with string concatenation. The backend WAF fails to flag the payload because the keyword `alert` is split during network transport.
* *Vector:* `top['al' + 'ert']`

### 💡 Parentheses Evasion (Execution via Template Literals)
To invoke the function while adapting to the restricted `()` token policy, the payload leverages **ECMAScript 6 (ES6) Template Literals** via backticks (`` ` ``). In modern JavaScript engines, writing `function` \`argument\` implicitly evaluates and executes the underlying function identically to a standard `function(argument)` call.
* *Vector:* `top['al'+'ert']` \`XSS\`

### 💡 Network Transport Sanitization (URL Encoding)
To prevent the string concatenation operator (`+`) from being misparsed as a literal space by the web server during inbound HTTP request handling, the character is manually converted to its safe URL-encoded hex equivalent: `%2B`.

---

## 4. The Final Proof-of-Concept (PoC)
Combining all the distinct evasion vectors yields a single-line final payload that successfully misleads the server-side WAF and executes arbitrary client-side JavaScript:

```text
http://localhost:9000/render?path=<svg/onload=top['al'%2B'ert']`GRID_NODE:_`%2Blocation.host>

#### 📷 Evidence of Exploitation
![WAF Evasion Success](poc.png)
