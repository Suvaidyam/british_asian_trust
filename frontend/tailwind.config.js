/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        poppins: ['Poppins'],
      },
      backgroundColor: {
        'primary': "var(--bg-primary)",
        'secondary': "var(--bg-secondary)",
      },

      textColor: {
        'primary': "var(--text-primary)",
        'secondary': "var(--text-secondary)",
      },
     
    },
  },
  plugins: [],
}
