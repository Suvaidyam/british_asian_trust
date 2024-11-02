/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Poppins'], // Make Poppins the default sans font
        // poppins: ['Poppins', 'sans-serif'], // Add a custom 'poppins' font option
      },
    },
  },
  plugins: [

  ]
}