const SudokuInputComponent = {
    delimiters: ['[[',']]'],
    el: "#sudoku_puzzle",
    data() {
        return {
            inputs: Array.from(
                        {length:9}, 
                        (r_val, r_id) => r_val = Array.from(
                            {length:9},
                            (c_val, c_id) => c_val = {
                                left_border: (c_id % 3 === 0 && c_id > 0),
                                top_border : (r_id % 3 === 0 && r_id > 0),

                            }
                        ),
                    ),
        }
    },
    template: `
      <table>
        <tr v-for="row in inputs">
            <td :class="{'left_border':col.left_border, 'top_border':col.top_border}" v-for="col in row">
            <input type="text" maxlength="1" @keypress="validateField">
            </td>
        </tr>
       </table>`,
    methods: {
        validateField(e){
            if (e.key < '1' || e.key > '9') {
                e.preventDefault();
            }else{
                // isSudokuFormValid()
                const button = document.querySelector('button')
                button.disabled = false
            }
        }
    }
}

const SudokuFieldsApp = {
    delimiters: ['[[',']]'],
    el: "#sudoku_puzzle",
    data() {
        return {
            disabled:false
        }
    },
    components:{
        'sudoku-input': SudokuInputComponent
    },
}

const app = Vue.createApp(SudokuFieldsApp)
app.mount("#sudoku_puzzle")