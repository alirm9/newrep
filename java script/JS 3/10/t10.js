'use strict';

const candidateCount = Number(prompt('Enter the number of candidates:'));
const candidates = [];

for (let i = 0; i < candidateCount; i++) {
  const name = prompt(`Name for candidate ${i + 1}:`);
  candidates.push({
    name: name,
    votes: 0,
  });
}

const voterCount = Number(prompt('Enter the number of voters:'));

for (let i = 0; i < voterCount; i++) {
  const vote = prompt(`Voter ${i + 1}, enter candidate name (leave empty for blank vote):`);
  if (vote) {
    const candidate = candidates.find(
      (c) => c.name.toLowerCase() === vote.trim().toLowerCase()
    );
    if (candidate) {
      candidate.votes++;
    }
  }
}

candidates.sort((a, b) => b.votes - a.votes);

console.log(`The winner is ${candidates[0].name} with ${candidates[0].votes} votes.`);
console.log('results:');
for (const c of candidates) {
  console.log(`${c.name}: ${c.votes} votes`);
}