document.addEventListener('DOMContentLoaded', function () {
    const evaluationInput = document.getElementById('id_evaluation');
    const stars = document.querySelectorAll('.evaluation i');

    stars.forEach(function (star) {
        star.addEventListener('click', function () {
            evaluationInput.value = this.dataset.value;
            evaluationInput.dispatchEvent(new Event('change'));
        });
    });

    evaluationInput.addEventListener('change', coloredStars);

    function coloredStars () {
        stars.forEach(function (star) {
            star.classList.remove('red-text');
            star.classList.add('grey-text');
        });

        for (let i = 0; i < evaluationInput.value; i++) {
            stars[i].classList.remove('grey-text');
            stars[i].classList.add('red-text');
        }
    }

    coloredStars();
});
