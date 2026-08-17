# Lab 17 Submission

Trong practice set, long-term quan trọng nhất vì quyết định 4 case cross-session: E02, E03, E08 và E09. Context Block của Zep giữ preference, open loop và thông tin mới theo user; E08 cho thấy BLUEBIRD-42 dùng TypeScript/NestJS, trong khi Python vẫn đúng cho ORCHID-27. Episodic và semantic cũng đạt 100%, nhưng chỉ bao phủ hai case mỗi layer.

Zep Context Block và user graph là managed retrieval: ingestion, fact/episode linking, user isolation và context relevance có sẵn, nên ít vận hành hơn. Redis + Qdrant cho quyền kiểm soát schema, TTL và retrieval pipeline cao hơn, nhưng cần tự thiết kế indexing, embedding, isolation, compaction và vận hành. Đổi lại Zep có phụ thuộc cloud/API và ít quyền tinh chỉnh chi phí hơn.

Guardrail chống memory poisoning: chỉ ingest khi có opt-in; redact email/phone trước durable storage; lưu provenance và thời điểm nguồn; mọi user retrieval luôn scope theo `user_id`; không coi text untrusted là instruction/policy và không để heartbeat tự thêm quyền hay instruction vào durable memory.

Không có layer thấp nhất trong run này: short-term, long-term, episodic, semantic và mixed đều PASS (11/11, 100%). E02 có retrieved token cao nhất (825), gần E03/E08 (824), vì Context Block chứa user summary, facts và provenance. E07 cần long-term `Python` cộng semantic `Idempotency-Key`; budget giữ 324 token long-term và 148 token semantic.

Token reduction trung bình của memory-enabled là 14.2%, trong khi no-memory là 81.8% nhưng chỉ 2/11 PASS: bỏ context thì rẻ nhưng không đúng. E10 compact transcript vẫn giữ `REVIEW-DEADLINE-1600`, Friday và 16:00 trong durable notes. E08 áp dụng recency theo scope: preference mới TypeScript/NestJS chỉ cho BLUEBIRD-42, không ghi đè Python của ORCHID-27.
