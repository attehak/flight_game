const chatButton = document.getElementById('chatToggle');
const chatbox = document.getElementById('chatbox');
const closeChat = document.getElementById('closeChat');
const messages = document.getElementById('messages');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');

// Open Chat
chatButton.addEventListener('click', () => {
  chatbox.style.display = 'flex';
  chatButton.style.display = 'none';
});

// Close Chat
closeChat.addEventListener('click', () => {
  chatbox.style.display = 'none';
  chatButton.style.display = 'flex';
});

// Send message
sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', e => {
  if (e.key === 'Enter') sendMessage();
});

function sendMessage() {
  const text = userInput.value.trim();
  if (text === '') return;

  const playerMsg = document.createElement('div');
  playerMsg.className = 'message player';
  playerMsg.textContent = text;
  messages.appendChild(playerMsg);
  userInput.value = '';
  messages.scrollTop = messages.scrollHeight;

  // Bot response
  setTimeout(() => {
    const hostMsg = document.createElement('div');
    hostMsg.className = 'message host';
    hostMsg.textContent = getHostReply(text);
    messages.appendChild(hostMsg);
    messages.scrollTop = messages.scrollHeight;
  }, 700);
}

function getHostReply(text) {
  text = text.toLowerCase();

  if (text.includes('apu') || text.includes('ongelma'))
    return "Kerro vain, mikä ongelma sinulla on, niin autan.";

  if (text.includes('lento') || text.includes('pelata'))
    return "Pidä kone vakaana ja tarkista polttoaineen määrä.";

  if (text.includes('hei') || text.includes('moi'))
    return "Hei! Kiva nähdä sinut taas!";

  return "Selvä! Välitän viestisi eteenpäin.";
}
