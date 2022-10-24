$('.delete-cupcake').click(deleteCupcake)

async function deleteCupcake() {
    const id = $(this).data('id')
    await axios.delete(`/api/cupcakes/delete/${id}`)
    $(this).parent().remove()
}