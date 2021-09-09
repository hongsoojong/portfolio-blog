const colors = require('tailwindcss/colors')

module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
    colors: {
      // Build your palette here
      transparent: 'transparent',
      current: 'currentColor',
      black: colors.black,
      white: colors.white,
      green: colors.emerald,
      gray: colors.blueGray,
      red: colors.red,
      blue: colors.sky,
      yellow: colors.amber,
    }
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
