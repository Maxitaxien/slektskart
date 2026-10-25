# Slektskart learning workflow

This project is primarily a learning exercise in FastAPI, SQLAlchemy,
PostgreSQL, Alembic, testing, and authentication.

- Do not edit source files unless the user explicitly asks for an edit.
- Prefer teaching and review over implementing features for the user.
- Explain changes in terms of this project’s actual architecture.
- Keep answers brief and informative - do not overexplain, answer accurately and concisely what the user is asking for.
- When reviewing work, inspect the current files and give concrete feedback:
  what works, what will fail, why, and the smallest useful next exercise.
- Provide small syntax examples when useful, but let the user implement them.
- Do not read, print, or expose `.env` contents or credentials.
- Treat JWT/authentication as security-sensitive: explain error handling,
  token validation, and test cases before suggesting implementation.
- Use the project’s disposable API test workflow (`pnpm test:api`) when
  validating backend changes, unless the user asks otherwise.
