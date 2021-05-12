//Object Initialisation
const cryptoapi = new cryptoAPI();
const ui = new UI();

const form=document.getElementById('form');

form.addEventListener('submit', async (event)=>{
    event.preventDefault();

    const currencySelect=document.getElementById('currency').value;

    const result = document.getElementById('result')

    const cryptoCurrencySelect=document.getElementById('cryptocurrency').value;

    // validating that the select have something
    if(currencySelect===''||cryptoCurrencySelect===''){
        ui.printMessage('All the Fields are mandatory','deep-orange darken-4 card-panel');
    }
    else{
        //Query the REST API
        const data = await fetch(`https://bitpay.com/api/rates/${cryptoCurrencySelect}/${currencySelect}`)
        const response = await data.json()
        result.innerHTML = response.rate;
        console.log(response)
    }
})