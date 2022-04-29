// const checkbox = document.getElementById('checkbox');
const checkbox = document.querySelector('.checkbox');
console.log(checkbox);

checkbox.addEventListener('click',toggleClick);

// function click() {
//     if(document.body.classList.contains('dark')){
//         document.body.classList.remove('dark');
//     } else {
//         document.body.classList.add('dark');
//         console.log('convert into Dark Mode');
//     }
//     // classlist = js가 css를...
// }

// toggle
function toggleClick() {
    document.body.classList.toggle('dark');
    console.log('Working!');

}