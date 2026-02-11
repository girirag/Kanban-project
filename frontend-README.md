# Kanban Board - Frontend

A modern Kanban board application built with SvelteKit, TypeScript, and Tailwind CSS.

## Features

- 🎯 Drag and drop tasks between columns
- 🎨 Clean, responsive UI with Tailwind CSS
- 🔥 Firebase integration for real-time data
- ⚡ Fast and lightweight with SvelteKit
- 📱 Mobile-friendly design

## Prerequisites

- Node.js 18+ and npm
- Firebase project (for backend integration)

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd kanban-frontend
```

2. Install dependencies:
```bash
npm install
```

3. Configure Firebase:
   - Update the Firebase configuration in `src/lib/firebase.ts` with your project credentials

4. Configure API endpoint:
   - Update the API URL in `src/lib/api.ts` to point to your backend server

## Development

Start the development server:
```bash
npm run dev
```

The app will be available at `http://localhost:5173`

## Building for Production

Create a production build:
```bash
npm run build
```

Preview the production build:
```bash
npm run preview
```

## Project Structure

```
src/
├── lib/
│   ├── api.ts          # API client for backend
│   ├── firebase.ts     # Firebase configuration
│   └── assets/         # Static assets
├── routes/
│   ├── +layout.svelte  # Root layout
│   └── +page.svelte    # Main Kanban board page
├── app.css             # Global styles
└── app.html            # HTML template
```

## Technologies

- [SvelteKit](https://kit.svelte.dev/) - Web framework
- [TypeScript](https://www.typescriptlang.org/) - Type safety
- [Tailwind CSS](https://tailwindcss.com/) - Styling
- [Firebase](https://firebase.google.com/) - Backend services
- [svelte-dnd-action](https://github.com/isaacHagoel/svelte-dnd-action) - Drag and drop

## Backend

This frontend requires the Kanban Board backend API. Find it at:
[kanban-backend repository](https://github.com/girirag/kanban-backend)

## License

MIT
