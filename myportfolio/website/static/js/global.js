$(document).ready(function(){
    $('.tutorial-category-img').click(function(e){
        let selected = $(this).attr('data-type');
        // hide category selector imgs
        $('.tutorial-category-img').hide(500);

        // show the selected category
        $(`.selected-category[data-type=${selected}]`).slideToggle(500);
    });

    $('.close-tutorial-selected').click(function(e){
        $('.tutorial-category-img').show();
        $('.selected-category').hide();
    });
});