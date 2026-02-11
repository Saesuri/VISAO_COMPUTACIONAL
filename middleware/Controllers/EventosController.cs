using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using middleware.Data;
using middleware.Models;

namespace middleware.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class EventosController : ControllerBase
    {
        private readonly AppDbContext _context;

        public EventosController(AppDbContext context)
        {
            _context = context;
        }

        [HttpPost]
        public async Task<IActionResult> Post([FromBody] Evento evento)
        {
            if (evento == null)
                return BadRequest();

            evento.DataHora = DateTime.Now;
            _context.Eventos.Add(evento);
            await _context.SaveChangesAsync();

            return Ok(new { mensagem = "Evento registrado!" });
        }

        [HttpGet]
        public async Task<IActionResult> Get()
        {
            var eventos = await _context.Eventos.OrderByDescending(e => e.DataHora).ToListAsync();

            return Ok(eventos);
        }
    }
}
