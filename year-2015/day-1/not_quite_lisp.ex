defmodule NotQuiteLisp do
  def part_one do
    {:ok, file} = File.read("instructions.txt")

    steps = String.to_charlist(file)
    {_, floor} = Enum.map_reduce(steps, 0,
      fn x, acc ->
        acc = (if x == 40, do: acc + 1, else: acc - 1)
        {x, acc}
      end
    )

    IO.puts(floor)
  end

  def part_two do
    {:ok, file} = File.read("instructions.txt")
    steps = String.to_charlist(file)

    IO.puts(take_step(0, steps, 0))
  end

  def take_step(step_count, _, -1) do
    step_count
  end

  def take_step(step_count, [step_to_take|remaining_steps], floor) do
    step_count = step_count + 1
    floor = (if step_to_take == 40, do: floor + 1, else: floor - 1)
    take_step(step_count, remaining_steps, floor)
  end

end

NotQuiteLisp.part_one
NotQuiteLisp.part_two
