const urlAPI = 'http://localhost:5105/api/eventos';

//  CONTADORES DE OBJETOS ATUALIZADOS

let contagemObjetos = {
    vermelho: 0,
    verde: 0,
    amarelo: 0,
    azul: 0,
    rosa: 0,
    roxo: 0,
    laranja: 0,
    total: 0
};

// Função para atualizar os números no painel HTML
function atualizarPainel() {
    // Mapeamento de ID do HTML para a chave no objeto contagemObjetos
    const mapaCores = {
        'count-red': 'vermelho',
        'count-green': 'verde',
        'count-yellow': 'amarelo',
        'count-blue': 'azul',
        'count-pink': 'rosa',
        'count-purple': 'roxo',
        'count-orange': 'laranja',
        'count-total': 'total'
    };

    // Percorre o mapa e atualiza apenas os elementos que existirem no HTML
    for (let id in mapaCores) {
        const elemento = document.getElementById(id);
        if (elemento) {
            const chaveObjeto = mapaCores[id];
            elemento.textContent = contagemObjetos[chaveObjeto];
        }
    }
}

// ~~~~ FUNÇÃO PARA ACESSAR A CÂMERA ~~~
async function iniciarCamera() {
    const video = document.getElementById('webcam');
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;
    } catch (err) {
        console.error("Erro ao acessar a webcam: ", err);
        const statusDiv = document.getElementById('status-conexao');
        if (statusDiv) statusDiv.innerHTML += ' | 📷 Câmera offline';
    }
}

// ~~ FUNÇÃO DE BUSCA DE EVENTOS ~~~~
async function buscarEventos() {
    try {
        const resposta = await fetch(urlAPI);
        
        if (!resposta.ok) throw new Error("Falha na requisição");

        const eventos = await resposta.json();
        const container = document.getElementById('lista-eventos');
        const statusDiv = document.getElementById('status-conexao');

        if (container) {
            container.innerHTML = ''; // Limpa a lista para atualizar
            eventos.forEach(evento => {
                const item = document.createElement('li');            
                item.textContent = `${evento.descricao} - ${new Date(evento.data).toLocaleString('pt-BR')}`;
                container.appendChild(item);
            });
        }

        if (statusDiv) {
            statusDiv.innerHTML = `🟢 API Online - Última atualização: ${new Date().toLocaleTimeString()}`;
        }

    } catch (erro) {
        console.error('Erro ao buscar dados:', erro);
        const statusDiv = document.getElementById('status-conexao');
        if (statusDiv) statusDiv.innerHTML = '🔴 Erro de conexão com o servidor local';
    }
}

// ~~~~ FUNÇÃO PARA REGISTRAR DETECÇÕES ~~~~
function registrarDeteccao(cor) {
    // Se a cor existir no nosso objeto, incrementa ela e o total
    if (contagemObjetos.hasOwnProperty(cor)) {
        contagemObjetos[cor]++;
        contagemObjetos.total++;
        atualizarPainel();
    } else {
        console.warn(`A cor "${cor}" não está configurada nos contadores.`);
    }
}

// ~~~~ INICIALIZAÇÃO ~~~~
iniciarCamera(); 
buscarEventos();
atualizarPainel(); // Define os valores iniciais (0) na tela

// Atualiza os dados da API a cada 3 segundos
setInterval(buscarEventos, 3000);
