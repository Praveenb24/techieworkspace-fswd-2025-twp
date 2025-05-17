class Toast {

    constructor () {

        this.toastContainer = document.getElementById("toast-container");

    }

    show (title, message) {

        const templateElement = document.createElement("template"),
            that = this;

        templateElement.innerHTML = this.template(
            title,
            message
        );

        const toastElement = templateElement.content.firstChild;

        toastElement.querySelector(".btn-close").addEventListener(
            "click",
            (event) => {

                toastElement.remove();

            }
        );

        this.toastContainer.appendChild(toastElement);

    }

    template (title, message) {

        const htmlSnippet = `
            <div class="toast" role="alert">
              <div class="toast-header">
                <strong>${title}</strong>
                <button type="button" class="btn-close">X</button>
              </div>
              <div class="toast-body">
                ${message}
              </div>
            </div>
        `;

        return htmlSnippet.trim();

    }

}
