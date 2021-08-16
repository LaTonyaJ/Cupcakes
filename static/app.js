function generateCupcakeHTML(cupcake){
    return `
    <div>
        <img src='${cupcake.image}' class='img-thumbnail'>
        <ul class=''>
            <li>${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating} </li>
        </ul>
    </div>
    `;
}


async function showCupcakes(){
    const resp = await axios.get('/api/cupcakes')
    for (let cupcake of resp.data.cupcakes){
        add_me = generateCupcakeHTML(cupcake)
        $('#cupcakes_list').append(add_me)
    }
}

$('#add_cupcake').on('submit', async function(e){
    e.preventDefault();

    let flavor = $('#flavor').val();
    let size = $('#size').val();
    let rating = $('#rating').val();
    let image = $('#image').val();
    
    const make_cupcake = await axios.post('/api/cupcakes', {
        flavor,
        size,
        rating,
        image
    });

    let new_cupcake = generateCupcakeHTML(make_cupcake.data.cupcake);
    $('#cupcakes_list').append(new_cupcake);
    $('#add_cupcake').trigger('reset');
}); 

showCupcakes();