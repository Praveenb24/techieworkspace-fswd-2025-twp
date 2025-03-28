class Auth {

    constructor () {

        const that = this;

        this.form = $("form");
        this.form.on(
            "submit",
            (event) => {

                event.preventDefault();
                that.validate();

            }
        );

    }

    validate () {

        const password = $("input[name='password']").val(),
              username = $("input[name='username']").val();

        if (username === "" && password === "") {

            console.log("Username and password should not be empty");
            event.preventDefault();

        }

        if (!this.#validateUsername(username)) {

            console.log(`Username is invalid. Username should be 8 - 16 char,
                        lower case letter and digits.`);
            event.preventDefault();

        }

        if (!this.#validatePassword(password)) {

            console.log(`password is invalid. password should be 8 - 16 char,
                         lower and uppercase case letter and digits.`);
            event.preventDefault();

        }

        console.log('Username and password are valid');

    }

    #validateUsername (username) {

        /*
         *  Limitation
         *  Username should not be empty
         *  Username should be 8 - 16 char.
         *  username should be lower a-z char and 0-9 digits
         */
        const regexPattern = /^[a-z0-9]{8,16}$/u;

        return regexPattern.test(username);

    }

    #validatePassword (password) {

        /*
         *  Limitation
         *  Password should not be empty
         *  Passowrd should be 8 - 16 char.
         *  Password should be any combination of lower a-z, upper A-Z, 0-9 digits and symbols $#@!.
         */
        const regexPattern = /^[a-zA-Z0-9@$#]{8,16}$/u;

        return regexPattern.test(password);

    }

}


// Without jQuery
// class Auth {

//     constructor () {

//         const that = this;

//         this.form = document.querySelector("form");
//         this.form.addEventListener(
//             "submit",
//             (event) => {

//                 event.preventDefault();
//                 that.validate();

//             }
//         );

//     }

//     validate () {

//         if (this.form.elements.username.value === "" &&
//            this.form.elements.password.value === "") {

//             console.log("Username and password should not be empty");
//             event.preventDefault();

//         }

//         if (!this.#validateUsername()) {

//             console.log(`Username is invalid. Username should be 8 - 16 char,
//                         lower case letter and digits.`);
//             event.preventDefault();

//         }

//         if (!this.#validatePassword()) {

//             console.log(`password is invalid. password should be 8 - 16 char,
//                          lower and uppercase case letter and digits.`);
//             event.preventDefault();

//         }

//         console.log('Username and password are valid');

//     }

//     #validateUsername () {

//         /*
//          *  Limitation
//          *  Username should not be empty
//          *  Username should be 8 - 16 char.
//          *  username should be lower a-z char and 0-9 digits
//          */
//         const regexPattern = /^[a-z0-9]{8,16}$/u;

//         return regexPattern.test(this.form.elements.username.value);

//     }

//     #validatePassword () {

//         /*
//          *  Limitation
//          *  Password should not be empty
//          *  Passowrd should be 8 - 16 char.
//          *  Password should be any combination of lower a-z, upper A-Z, 0-9 digits and symbols $#@!.
//          */
//         const regexPattern = /^[a-zA-Z0-9@$#]{8,16}$/u;

//         return regexPattern.test(this.form.elements.password.value);

//     }

// }


// Initial development
// class Auth {
//     constructor() {
//         let _this = this;
//         this.form = document.querySelector('form');
//         this.form.addEventListener('submit', function(event) {
//             event.preventDefault();
//             _this.validate();
//         });
//     }
//     validate() {
//         if(this.form.elements.username.value =='' && 
//            this.form.elements.password.value ==''){
//             console.log("Username and password should not be empty");
//             event.preventDefault();
//         }

//         if(!this.#validateUsername()) {
//             alert('Username is invalid. Username should be 8 - 16 char, lower case letter and digits.');
//             event.preventDefault();
//         }

//         if(!this.#validatePassword()) {
//             alert('password is invalid. password should be 8 - 16 char, lower and uppercase case letter and digits.');
//             event.preventDefault();
//         }
//     }
//     #validateUsername(){
//         //  Limitation
//         //  Username should not be empty
//         //  Username should be 8 - 16 char.
//         //  username should be lower a-z char and 0-9 digits
//         let regexPattern = /^[a-z0-9]{8,16}/u;
//         return regexPattern.test(this.form.elements.username.value)
//     }
//     #validatePassword(){
//         //  Limitation
//         //  Password should not be empty
//         //  Passowrd should be 8 - 16 char.
//         //  Password should be any combination of lower a-z, upper A-Z, 0-9 digits and symbols $#@!.
//         let regexPattern = /^[a-zA-Z0-9@$#]{8,16}/u;
//         regexPattern.test(this.form.elements.password.value)
//     }
// }