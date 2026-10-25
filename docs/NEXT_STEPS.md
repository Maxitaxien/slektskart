# Next step

Build the login UI flow:

1. Add visible fields and a submit button to `LoginForm`.
2. Send the form data to `POST /api/auth/login`.
3. Store the returned access token in React state.
4. Call `GET /api/auth/me` with `Authorization: Bearer <token>` and display the user.
