echo "Are you sure you want to create the following rule?"
echo "====="
echo "Account: $account"
echo "Comment: $comment"
echo "RSE: $rse_expression"
echo "Block: $block"
echo "Copies $copies"
echo "Lifetime: $lifetime seconds ($(expr $lifetime / 86400) days)"
echo "====="

select yn in "Yes" "No"; do
    case $yn in
        Yes ) rucio add-rule --account $account --lifetime $lifetime --comment "$comment" $block $copies $rse_expression ; break;;
        No ) echo "Aborting"; break;;
    esac
done
