async function checkPageStatus() {
  try {
    // Aqui você define a URL da página que quer verificar
    const response = await fetch('ldgfkbnmld~gkbnms~dg')
    if (response.status === 404) {
      window.location.href = '/erroPag' // Caminho da sua página de erro
    } else {
      console.log('Página encontrada ou outro status:', response.status)
    }
  } catch (error) {
    console.error('Erro ao verificar o status da página:', error)
  }
}
