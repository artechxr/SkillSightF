// app/config.ts
/**
 * Centralized configuration for the SkillSight frontend.
 * Reads environment variables provided by Next.js.
 * Uses NEXT_PUBLIC_API_URL for the backend API base URL.
 */
export const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8000/api";
