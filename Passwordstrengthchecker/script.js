function checkPasswordStrength(password) {
  let rulesPassed = 0;

  if (password.length >= 8) rulesPassed++;  // Rule 1
  if (/[a-z]/.test(password) && /[A-Z]/.test(password)) rulesPassed++; // Rule 2
  if (/[0-9]/.test(password)) rulesPassed++; // Rule 3
  if (/[!@#$%^&*]/.test(password)) rulesPassed++; // Rule 4

  if (rulesPassed < 2) return "weak";
  else if (rulesPassed < 4) return "medium";
  else return "strong";
}

function checkPassword() {
  let userPassword = document.getElementById("passwordInput").value;
  let strength = checkPasswordStrength(userPassword);

  let result = document.getElementById("result");
  result.innerText = "Password strength: " + strength;

  // Change color based on strength
  if (strength === "weak") {
    result.style.color = "red";
  } else if (strength === "medium") {
    result.style.color = "orange";
  } else {
    result.style.color = "green";
  }
}
