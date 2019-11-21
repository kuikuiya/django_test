var step_title = new Vue({
    delimiters: ['[[', ']]'],
    el: '#step_title',
    
    data: {
        
        titles:        
        [
            "1. Roll stats (능력치를 굴려요)",
            "2. 최대 건강",
            "3. 시작 특성",
            "4. 여섯가지 물품 선택",
            "5. 전투장비를 선택하세요.",
            "6. 겉모습",
            "7. 신체특징",
            "8. 뒷배경",
            "9. 옷차림",
            "10. 성격",
            "11. 말버릇",
            "12. 이름, 레벨, 경험치"
        ],

        numbers: [ 1, 2, 3, 4, 5 ],
        text: ""

    },
    methods: {
        ff: function (n) {
            this.text = n;
          //  alert(n);
        }
        ,

        tt: function (titles) {
            //this.step_title = this.title[step] 
            return titles.filter(function(t) {
                return t.charAt(0) % 3 === 0
            })
        }

        
    }
/*
    data: {
        nubers: [ 1, 2, 3, 4, 5 ]
    },
    computed: {
        evenNumbers: function () {
          return this.numbers.filter(function (number) {
            return number % 2 === 0
            })
        }
    }  */
})
/*
var step = 1;

function print_step_text(step)
{
    //document.getElementById('step_title').innerText = step_title[step - 1]
}
*/
