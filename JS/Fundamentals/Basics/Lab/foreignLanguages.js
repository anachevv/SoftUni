function speak(country) {
    const countries = {"English": ["England", "USA"], "Spanish": ["Spain", "Argentina", "Mexico"]};

    for (const [key, value] of Object.entries(countries)) {
        for (let idx = 0; idx < value.length; idx++) {
            if (value[idx] === country) {
                return key;
            }
        }
      }
      return "unknown";
}

console.log(speak("USA"));
