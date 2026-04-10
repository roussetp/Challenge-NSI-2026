function corriger() {
  let score = 0;
  const totalQuestions = 5;

  for (let i = 1; i <= totalQuestions; i++) {
    const reponse = document.querySelector('input[name="q' + i + '"]:checked');
    if (reponse) {
      score += parseInt(reponse.value);
    }
  }

  const resultat = document.getElementById("resultat");

  if (score === totalQuestions) {
    resultat.textContent = "🏆 Parfait ! 5/5 ! Tu maîtrises bien les biomes Minecraft !";
  } else if (score >= 4) {
    resultat.textContent = "👏 Très bon score : " + score + " / " + totalQuestions;
  } else if (score >= 2) {
    resultat.textContent = "🙂 Score correct : " + score + " / " + totalQuestions;
  } else {
    resultat.textContent = "😅 Score faible : " + score + " / " + totalQuestions;
  }
}