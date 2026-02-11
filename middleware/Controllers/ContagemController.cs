using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using middleware.Data;
using middleware.Models;

namespace middleware.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ContagemController : ControllerBase
    {
        private readonly AppDbContext _context;

        public ContagemController(AppDbContext context)
        {
            _context = context;
        }

        [HttpGet("resumo24h")]
        public async Task<IActionResult> GetResumo()
        {
            var umDiaAtras = DateTime.Now.AddHours(-24);

            var estatisticas = await _context
                .Eventos.Where(e => e.DataHora >= umDiaAtras)
                .GroupBy(e => e.Cor)
                .Select(grupo => new { Categoria = grupo.Key, Total = grupo.Count() })
                .ToListAsync();

            return Ok(estatisticas);
        }
    }
}
