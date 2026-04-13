def run():              
    task_name = "email_triage"

    print(f"[START] task={task_name}", flush=True)

    # Example step (you can connect your logic here)
    step = 1
    reward = 0.5
    print(f"[STEP] step={step} reward={reward}", flush=True)

    # Final output
    score = 0.95
    steps = 1
    print(f"[END] task={task_name} score={score} steps={steps}", flush=True)


if __name__ == "__main__":
    run()
