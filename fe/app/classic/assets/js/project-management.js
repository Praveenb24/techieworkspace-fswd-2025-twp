// Procedural style
// let input = document.getElementById('todo-input');
// let btn = document.getElementById('todo-add-task');
// let ul = document.getElementById('todo-list');
// btn.addEventListener('click', function() {
//   if (input.value != '') {
//     let li = document.createElement('li');
//     li.innerText = input.value;
//     ul.appendChild(li);
//     input.value = '';
//   }
// });



// Object style.

// let  task = {
//     init: function() {
//        let _this = this;
//        this.stage = document.getElementById('todo');
//        this.form = this.stage.getElementsByTagName('form')[0];
//        this.form.addEventListener('submit', function(event) {
//             event.preventDefault();
//             _this.add();
//        });
//        this.list = this.stage.getElementsByTagName('ul')[0];
//     },
//     add: function() {
//         if (this.form.elements.task.value == '') {
//             return;
//         }
//         let _this = this;

//         let li = document.createElement('li');

//         let checkbox = document.createElement('input');
//         checkbox.type = 'checkbox';

//         let span = document.createElement('span');
//         span.innerText = this.form.elements.task.value;

//         let btn = document.createElement('button');
//         btn.innerText = 'Delete';
//         btn.addEventListener('click',function(event){
//             _this.remove(li);
//         });

//         li.appendChild(checkbox);
//         li.appendChild(span);
//         li.appendChild(btn);

//         this.list.appendChild(li);
//         this.form.elements.task.value = '';
//     },
//     remove: function(li) {
//         li.remove();
//     }
// }


// Prototype based Object style
// function Task(stagename) {
//    let _this = this;
//    this.stage = document.getElementById(stagename);
//    this.form = this.stage.getElementsByTagName('form')[0];
//    this.form.addEventListener('submit', function(event) {
//         event.preventDefault();
//         _this.add();
//    });
//    this.list = this.stage.getElementsByTagName('ul')[0];
// }

// Task.prototype.add = function() {
//     if (this.form.elements.task.value == '') {
//         return;
//     }
//     let _this = this;

//     let li = document.createElement('li');

//     let checkbox = document.createElement('input');
//     checkbox.type = 'checkbox';

//     let span = document.createElement('span');
//     span.innerText = this.form.elements.task.value;

//     let btn = document.createElement('button');
//     btn.innerText = 'Delete';
//     btn.addEventListener('click',function(event){
//         _this.remove(li);
//     });

//     li.appendChild(checkbox);
//     li.appendChild(span);
//     li.appendChild(btn);

//     this.list.appendChild(li);
//     this.form.elements.task.value = '';
// }

// Task.prototype.remove = function(li) {
//     li.remove();
// }


// Class based OOPs style
class Task {

    // default method for initializing class / object.
    constructor(stagename) {
       let _this = this;
       this.stage = document.getElementById(stagename);
       this.form = this.stage.getElementsByTagName('form')[0];
       this.form.addEventListener('submit', function(event) {
            event.preventDefault();
            _this.add();
       });
       this.list = this.stage.getElementsByTagName('ul')[0];
    }

    add() {
        if (this.form.elements.task.value == '') {
            return;
        }
        let _this = this;

        let li = document.createElement('li');

        let checkbox = document.createElement('input');
        checkbox.type = 'checkbox';

        let span = document.createElement('span');
        span.innerText = this.form.elements.task.value;

        let btn = document.createElement('button');
        btn.innerText = 'Delete';
        btn.addEventListener('click',function(event){
            _this.remove(li);
        });

        li.appendChild(checkbox);
        li.appendChild(span);
        li.appendChild(btn);

        this.list.appendChild(li);
        this.form.elements.task.value = '';
    }

    remove(li) {
        li.remove();
    }

}


// class ToDo extends Task {
//     add() {
//         alert('Extended add method called.');
//     }
//     update() {
//         console.log('update method called.');
//     }
// }