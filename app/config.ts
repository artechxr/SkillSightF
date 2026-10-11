```ts
// app/config.ts
/**
 * Centralized configuration for the SkillSight frontend.
 * Uses NEXT_PUBLIC_API_URL for the backend API base URL.
 */
export const API_URL =
  process.env.NEXT_PUBLIC_API_URL ??
  "https://skillsightf.onrender.com/api";
