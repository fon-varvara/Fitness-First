fn main() {
    // Initialize and print welcome message
    println!("Welcome to Fitness First!"); 
    
    // Define user data
    let age: u16 = 18;
    let height: u16 = 167;
    let weight: u16 = 70;
    
    // Ask user to input fitness goals
    println!("What are your fitness goals?");
    let mut goals = String::new();
    std::io::stdin().read_line(&mut goals).expect("Failed to read");

    // Compute BMI
    let bmi: f32 = (weight as f32 / (height as f32).powi(2)) * 703.0;
    println!("Your BMI is {}.", bmi);

    // Determine overweight status
    let overweight: bool;
    if bmi >= 25.0 {
        overweight = true;
    } else {
        overweight = false;
    }

    // Estimate calories required
    let cal_req: u16;
    if overweight {
        cal_req = (weight * (30 + (age / 10) + 6) + 5) * 10;
    } else {
        cal_req = (weight * (30 + (age / 10) - 6) + 5) * 10;
    }
    println!("Your estimated calorie requirement is {} per day.", cal_req);

    // Provide muscle building and cardio programs
    println!("We have the following programs for you to choose from:");
    println!("1. Muscle Building");
    println!("2. Cardio");
    println!("Please choose a program:");
    let mut program = String::new();
    std::io::stdin().read_line(&mut program).expect("Failed to read");
    let program: u8 = program.trim().parse().expect("Please type a number!");

    // Program selection
    let program_opt = match program {
        1 => {
            println!("You have chosen the Muscle Building program. Please refer to our gym instructor for more details.");
            "Muscle Building"
        },
        2 => {
            println!("You have chosen the Cardio program. Please refer to our gym instructor for more details.");
            "Cardio"
        },
        _ => {
            println!("Please choose either the Muscle Building or Cardio program.");
            ""
        }
    };

    // Define user goals and target
    let goals = goals.trim();
    let target = if program_opt == "Muscle Building" {
        println!("For muscle building program, which muscle group would you like to target?");
        let mut target_muscle = String::new();
        std::io::stdin().read_line(&mut target_muscle).expect("Failed to read");
        Some(target_muscle)
    } else if program_opt == "Cardio" {
        println!("For cardio program, which type of cardio would you like to do?");
        let mut target_cardio = String::new();
        std::io::stdin().read_line(&mut target_cardio).expect("Failed to read");
        Some(target_cardio)
    } else {
        None
    };

    // Create goals statement and store in the database
    let goals_statement = format!("My goal is to {} and my target is to {}.", goals, target.unwrap_or("".to_string())); 
    println!("{}", goals_statement);

    // Print goodbye message and exit
    println!("Thank you for joining Fitness First. Goodbye!");
}