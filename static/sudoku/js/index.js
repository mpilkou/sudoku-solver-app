
const App = {
    data() {
        return {
            product:"Sudoku"
        }
    }
}

const app = Vue.createApp(App)
app.config.compilerOptions.delimiters = ['[[',']]']

app.mount("#sudoku_div")
