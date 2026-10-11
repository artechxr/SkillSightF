// app/config.ts
/**
 * Centralized configuration for the SkillSight frontend.
 * Reads environment variables provided by Next.js.
 * Uses NEXT_PUBLIC_API_URL for the backend API base URL.
 */
```ts
export const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "https://skillsightf.onrender.com/api";
```
