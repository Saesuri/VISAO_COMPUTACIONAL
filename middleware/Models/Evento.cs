namespace middleware.Models
{
    public class Evento 
    {
        public int Id { get; set; }
        public string Cor { get; set; } = string.Empty;   
        public string CameraId { get; set; } = string.Empty; // Adicionado = string.Empty
        public DateTime DataHora { get; set; }
    }
}