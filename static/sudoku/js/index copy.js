isSudokuFormValid = () => {
    let inputs_list = [];
    for ( let tr of document.getElementById("sudoku_puzzle").getElementsByTagName("tr")){
        inputs_list.push([tr.getElementsByTagName("input")])
    }
    console.log(inputs_list)
    return true
}

const SudokuInputComponent = {
    delimiters: ['[[',']]'],
    el: "#sudoku_puzzle",
    data() {
        return {
            inputs: 
            [
                [
                    {
                        col_id: 0,
                        row_id: 0,
                        value:'',
                        error: false,
                        left_border: false,
                        top_border:  false,
                    },
                    {
                        col_id: 1,
                        row_id: 0,
                        value:'',
                        error: false,
                        left_border: false,
                        top_border:  false,
                    },
                    {
                        col_id: 2,
                        row_id: 0,
                        value:'',
                        error: false,
                        left_border: false,
                        top_border:  false,
                    }
                ],
                [
                    {
                        col_id: 0,
                        row_id: 1,
                        value:'',
                        error: false,
                        left_border: false,
                        top_border:  false,
                    },
                    {
                        col_id: 1,
                        row_id: 1,
                        value:'',
                        error: false,
                        left_border: false,
                        top_border:  false,
                    },
                    {
                        col_id: 2,
                        row_id: 1,
                        value:'',
                        error: false,
                        left_border: false,
                        top_border:  false,
                    }
                ],
                [
                    {
                        col_id: 0,
                        row_id: 2,
                        value:'',
                        error: false,
                        left_border: false,
                        top_border:  false,
                    },
                    {
                        col_id: 1,
                        row_id: 2,
                        value:'',
                        error: false,
                        left_border: false,
                        top_border:  false,
                    },
                    {
                        col_id: 2,
                        row_id: 2,
                        value:'',
                        error: false,
                        left_border: false,
                        top_border:  false,
                    }
                ],
            ]
            // Array.from(
            //             {length:9},
            //             (r_val, r_id) => r_val = Array.from(
            //                 {length:9},
            //                 (c_val, c_id) => c_val = {
            //                     col_id: c_id,
            //                     row_id: r_id,
            //                     sqr_id: Math.floor(c_id/3)+Math.floor(r_id/3),
            //                     value: '',
            //                     left_border: (c_id % 3 === 0 && c_id > 0),
            //                     top_border:  (r_id % 3 === 0 && r_id > 0),
            //                 }
            //             ),
            //         ),
        }
    },
    template: 
      `<table>
        <tr v-for="row in inputs">
            <td :class="{'left_border':col.left_border, 'top_border':col.top_border}" v-for="col in row">
            <input type="text" maxlength="1" :class="{'error':col.error}"
            :key="col.value"
            v-model="col.value"
            @keypress="validateField(col.row_id, col.col_id, col.value)">
            </td>
        </tr>
      </table>`,
    //   :value="values" @input="$emit('update:values', $event.target.value)"
    //   v-model="col.value"
    // @keypress='validateField(col.row_id, col.col_id, "update:values")
    //   :value='col.value' 

    methods: {
        initFields(){
            for (const row of this.inputs) {
                for (const col of row) {
                    col.value = ''
                }
            }
        },
        validateField(row_id, col_id, value){
            console.log(row_id)
            console.log(col_id)
            console.log(value)
            let aval = this.inputs[row_id][col_id].value
            console.log(aval)
            
            // let {value} = this.inputs[row_id][col_id]
            // console.log(typeof(value))
            // console.log(value === 1)
            // console.log(value)
            // console.log(aval)
            // console.log(this.inputs[row_id][col_id].value < '9' && this.inputs[row_id][col_id].value > '1')

            // console.log(this.values)
            // console.log(this)
            // console.log(this.inputs[row_id][col_id].error)
            // this.inputs[row_id][col_id].error = true

            // this.values = 9
            // console.log(this.inputs[row_id][col_id].value)
            // for (let i = 0; i < 9; i++) {
            //     for (let j = 0; j < 9; j++) {
            //         if (!(i === row_id && j === col_id) && this.value[i][j] === value) {
            //             this.value[row_id][col_id].error = true
            //         }else{
            //             this.value[i][j].error = false
            //         }
                    
            //     }
            // }
            // console.log(this.inputs.filter((r_list) => ))
            // col.col_id, col.row_id, col.value
            // if (e.key < '1' || e.key > '9') {
            //     e.preventDefault();
            // }else{
            //     // isSudokuFormValid()
            //     const button = document.querySelector('button')
            //     button.disabled = false
            // }

        }
    },
    // mounted() {
    //     this.initFields()
    // }
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
    computed:{
        // inputsArrayCreator(x){
        //     return Array.from({length:9},)
        // }
        //  = (i) => Array.from(
        //     {length:9}, 
        //     (val,j) => val
            // ={
            //     c_id: j,
            //     r_id: i,
            //     left_border: true, //(this.c_id % 3 === 0 && this.c_id > 0), 
            //     top_border : true,//(this.r_id % 3 === 0 && this.r_id > 0)
            // }
    },
    methods: {
    }
}

const app = Vue.createApp(SudokuFieldsApp)
app.mount("#sudoku_puzzle")