/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      boxShadow: {
        btn: "rgba(0, 0, 0, 0.3) 0px 19px 38px,rgba(0, 0, 0, 0.22) 0px 15px 12px",
        bx:"#000000 0px 0px 10px",
        bx1:"#000000 0px 0px 5px",
      },
      fontFamily: {
        sans: ['Graphik', 'sans-serif'],
        inter:['Inter'],
      },
      backgroundImage: {
        "bw-pic1": "url('./assets/bg.jpg')",
      },
    },
  },
  plugins: [],
}