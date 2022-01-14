

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


let tr_list = document.getElementsByTagName("tr")

//tr_list[i].td_list = tr_list[i].getElementsByTagName("td");

for (let i = 0; i < tr_list.length; i++)
{
    tr_list[i].td_list = tr_list[i].getElementsByTagName("td");
    if ( i%3 == 0 && (i > 1))
    {
        tr_list[i].style = "border-top: 2px solid black";
    }
    for (let j = 0; j < tr_list[i].td_list.length; j++) {
        if ( j%3 == 0 && (j > 1))
        {
            tr_list[i].td_list[j].style = "border-left: 2px solid black"
        }
        
    }
}

// map
// list operations js

//     // for (let j = 1; j < list_j.length; j++) 
//     // {
//     //     if (j-2%3 == 0 && j < 8) {
//     //         list_j[j].style = "border-right: 2px solid black";    
//     //     }   
//     // }
//     if ( i%3 == 0 && (i < 8 && i == 1))
//     {
//         list_i[i].style = "border-bottom: 2px solid black";
//     }
//         // list[i].getElementsByTagName("input"));
