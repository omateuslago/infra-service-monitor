namespace InfraMonitorAPI.Models
{
    public class Service
    {
        public int Id { get; set; }
        public required string Name { get; set; }
        public required string Url { get; set; }
        public bool IsActive { get; set; } = true;
        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
        public List<ServiceCheck> Checks { get; set; } = [];
    }
}
