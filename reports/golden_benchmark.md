# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1242.0 ms**
- Average token reduction vs full source context: **6.3%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.6 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G08 | long_term | PASS | 1592.4 | 812 | 0.0% |  |
| G09 | long_term | PASS | 1655.9 | 1426 | 0.0% |  |
| G12 | semantic | PASS | 275.6 | 418 | 8.9% |  |
| G14 | semantic | PASS | 466.6 | 270 | 30.2% |  |
| G15 | semantic | PASS | 259.4 | 270 | 41.2% |  |
| G19 | mixed | PASS | 3669.0 | 581 | 0.0% |  |
| G03 | long_term | PASS | 1725.6 | 1426 | 0.0% |  |
| G04 | long_term | PASS | 1749.6 | 1408 | 0.0% |  |
| G05 | long_term | PASS | 2101.8 | 1406 | 0.0% |  |
| G10 | episodic | PASS | 298.2 | 582 | 0.0% |  |
| G11 | episodic | PASS | 295.8 | 613 | 0.0% |  |
| G13 | semantic | PASS | 341.3 | 416 | 26.4% |  |
| G16 | mixed | PASS | 1793.0 | 581 | 0.0% |  |
| G18 | mixed | PASS | 641.6 | 500 | 11.5% |  |
| G20 | mixed | PASS | 2348.4 | 831 | 0.0% |  |
| G06 | long_term | PASS | 1823.8 | 1419 | 0.0% |  |
| G07 | long_term | PASS | 1927.4 | 1409 | 0.0% |  |
| G17 | mixed | PASS | 1873.9 | 581 | 8.1% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G08 - long_term

`<USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend examples and do not use Python for the backend. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. </EPISOD`

### G09 - long_term

`<USER_SUMMARY> Minh Nguyen works on a personal project named ORCHID-27, for which they prefer using Python. For company projects, specifically BLUEBIRD-42, the backend must be developed using TypeScript with NestJS, and Python is not to be used for this project.  Minh Nguyen prefers Python and dislikes Java. When explaining code, the user prefers short examples. The user is learning async/await and may confuse coroutine with Task. For the ORCHID-27 project, the user found a solution to a connection churn issue by reusing an aiohttp ClientSession and setting concurrency to 20, which resolved the problem. Increasing the timeout was ineffective.  When explaining async/await, coroutine, and Task`

### G12 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, epis`

### G14 - semantic

`EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marke`

### G15 - semantic

`EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marke`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend examples and do not use Python for the backend. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend exampl`

### G03 - long_term

`<USER_SUMMARY> Minh Nguyen works on a personal project named ORCHID-27, for which they prefer using Python. For company projects, specifically BLUEBIRD-42, the backend must be developed using TypeScript with NestJS, and Python is not to be used for this project.  Minh Nguyen prefers Python and dislikes Java. When explaining code, the user prefers short examples. The user is learning async/await and may confuse coroutine with Task. For the ORCHID-27 project, the user found a solution to a connection churn issue by reusing an aiohttp ClientSession and setting concurrency to 20, which resolved the problem. Increasing the timeout was ineffective.  When explaining async/await, coroutine, and Task`

### G04 - long_term

`<USER_SUMMARY> Minh Nguyen works on a personal project named ORCHID-27, for which they prefer using Python. For company projects, specifically BLUEBIRD-42, the backend must be developed using TypeScript with NestJS, and Python is not to be used for this project.  Minh Nguyen prefers Python and dislikes Java. When explaining code, the user prefers short examples. The user is learning async/await and may confuse coroutine with Task. For the ORCHID-27 project, the user found a solution to a connection churn issue by reusing an aiohttp ClientSession and setting concurrency to 20, which resolved the problem. Increasing the timeout was ineffective.  When explaining async/await, coroutine, and Task`

### G05 - long_term

`<USER_SUMMARY> Minh Nguyen works on a personal project named ORCHID-27, for which they prefer using Python. For company projects, specifically BLUEBIRD-42, the backend must be developed using TypeScript with NestJS, and Python is not to be used for this project.  Minh Nguyen prefers Python and dislikes Java. When explaining code, the user prefers short examples. The user is learning async/await and may confuse coroutine with Task. For the ORCHID-27 project, the user found a solution to a connection churn issue by reusing an aiohttp ClientSession and setting concurrency to 20, which resolved the problem. Increasing the timeout was ineffective.  When explaining async/await, coroutine, and Task`

### G10 - episodic

`EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Minh dang setup lai moi truong dev cho mot buoi ngoi code mot minh cuoi tuan nay, kieu khong co ai chung nhom, chi lam project rieng cua minh cho vui thoi. Truoc khi minh chon temp EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession +`

### G11 - episodic

`EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Minh dang setup lai moi truong dev cho mot buoi ngoi code mot minh cuoi tuan nay, kieu khong co ai chung nhom, chi lam project rieng cua minh cho vui thoi. Truoc khi minh chon temp EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Cap nhat moi:`

### G13 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata= EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 per`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh Nguyen works on a personal project named ORCHID-27, for which they prefer using Python. For company projects, specifically BLUEBIRD-42, the backend must be developed using TypeScript with NestJS, and Python is not to be used for this project.  Minh Nguyen prefers Python and dislikes Java. When explaining code, the user prefers short examples. The user is learning async/await and may confuse coroutine with Task. For the ORCHID-27 project, the user found a solution to a connection churn issue by reusing an aiohttp ClientSession and setting concurrency to 20, which resolved the problem. Increasing the timeout was ineffective.  When explaining async/await, corouti`

### G18 - mixed

`<EPISODIC> EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Minh dang setup lai moi truong dev cho mot buoi ngoi code mot minh cuoi tuan nay, kieu khong co ai chung nhom, chi lam project rieng cua minh cho vui thoi. Truoc khi minh chon temp EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Voi demo ca nhan cua Minh, ngon ngu uu t`

### G20 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh Nguyen works on a personal project named ORCHID-27, for which they prefer using Python. For company projects, specifically BLUEBIRD-42, the backend must be developed using TypeScript with NestJS, and Python is not to be used for this project.  Minh Nguyen prefers Python and dislikes Java. When explaining code, the user prefers short examples. The user is learning async/await and may confuse coroutine with Task. For the ORCHID-27 project, the user found a solution to a connection churn issue by reusing an aiohttp ClientSession and setting concurrency to 20, which resolved the problem. Increasing the timeout was ineffective.  When explaining async/await, corouti`

### G06 - long_term

`<USER_SUMMARY> Minh Nguyen works on a personal project named ORCHID-27, for which they prefer using Python. For company projects, specifically BLUEBIRD-42, the backend must be developed using TypeScript with NestJS, and Python is not to be used for this project.  Minh Nguyen prefers Python and dislikes Java. When explaining code, the user prefers short examples. The user is learning async/await and may confuse coroutine with Task. For the ORCHID-27 project, the user found a solution to a connection churn issue by reusing an aiohttp ClientSession and setting concurrency to 20, which resolved the problem. Increasing the timeout was ineffective.  When explaining async/await, coroutine, and Task`

### G07 - long_term

`<USER_SUMMARY> Minh Nguyen works on a personal project named ORCHID-27, for which they prefer using Python. For company projects, specifically BLUEBIRD-42, the backend must be developed using TypeScript with NestJS, and Python is not to be used for this project.  Minh Nguyen prefers Python and dislikes Java. When explaining code, the user prefers short examples. The user is learning async/await and may confuse coroutine with Task. For the ORCHID-27 project, the user found a solution to a connection churn issue by reusing an aiohttp ClientSession and setting concurrency to 20, which resolved the problem. Increasing the timeout was ineffective.  When explaining async/await, coroutine, and Task`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh Nguyen works on a personal project named ORCHID-27, for which they prefer using Python. For company projects, specifically BLUEBIRD-42, the backend must be developed using TypeScript with NestJS, and Python is not to be used for this project.  Minh Nguyen prefers Python and dislikes Java. When explaining code, the user prefers short examples. The user is learning async/await and may confuse coroutine with Task. For the ORCHID-27 project, the user found a solution to a connection churn issue by reusing an aiohttp ClientSession and setting concurrency to 20, which resolved the problem. Increasing the timeout was ineffective.  When explaining async/await, corouti`
