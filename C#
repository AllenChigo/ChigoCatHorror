using System;
using System.Threading.Tasks;

public class ShadowCat {
    public float Distance = 10.0f;
    public bool IsAggressive = true;

    public async Task StartChase() {
        Console.WriteLine("You hear claws skittering on the hardwood...");

        while (Distance > 0) {
            // C# is great for precise timing and math
            float dashSpeed = new Random().Next(2, 5);
            Distance -= dashSpeed;

            Console.WriteLine($"The gray shadow is {Distance}m away.");
            
            if (Distance < 3) {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("THE CAT HISSES.");
                Console.ResetColor();
            }

            await Task.Delay(1000); // Wait 1 second
        }
        Console.WriteLine("Game Over. You feel the fur against your skin.");
    }
}
