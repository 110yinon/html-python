console.log('hi all');

const logPage = document.querySelector('.log');
logPage.addEventListener('click', e => {
  if (e.target.innerText.includes('Flow File')) {
    // console.dir(e.target);
    const summaryElement = e.target.nextElementSibling.nextElementSibling
    // console.dir(summaryElement);
    summaryElement.classList.toggle('invisible')
  }

  if(e.target.classList.contains('sub-test-name')){
    const subTestNameElem = e.target.nextElementSibling.nextElementSibling
    subTestNameElem.classList.toggle('invisible')
    // console.log(subTestNameElem)
  }
});

