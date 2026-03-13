namespace InfraMonitorAPI.Models
{
    public class ServiceCheck
    {
        public int Id { get; set; }

        public int ServiceId { get; set; }

        public bool IsOnline { get; set; }

        public int ResponseTimeMs { get; set; }

        public DateTime CheckedAt { get; set; } = DateTime.UtcNow;

        public Service? Service { get; set; }
    }
}