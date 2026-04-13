const output = document.getElementById("game-text");

async function typeEffect(text, color = "gray") {
    const p = document.createElement("p");
    p.style.color = color;
    output.appendChild(p);
    
    for (let char of text) {
        p.innerHTML += char;
        // Random "stutter" in typing for tension
        await new Promise(r => setTimeout(r, Math.random() * 50 + 20));
    }
}

async function startChase() {
    await typeEffect("The air in the house is heavy and damp...", "#555");
    await typeEffect("A pair of yellow eyes ignites in the corner.", "gold");
    await typeEffect("HHHHHHSSSSSS!", "red"); // The Hiss
    document.body.style.backgroundColor = "#1a0000"; // Flash dark red
}
