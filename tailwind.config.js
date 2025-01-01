/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["light", "dark"], // Choix des thèmes
  },
};

// npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --minify

// npx tailwindcss -i ./static/css/input.css -o ./dist/output.css --watch


